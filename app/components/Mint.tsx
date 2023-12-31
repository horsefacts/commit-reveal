import { BigNumberish, BytesLike, Interface } from "ethers";
import React, { useState } from "react";
import {
  useAccount,
  useContractWrite,
  useNetwork,
  usePrepareContractWrite,
  useWaitForTransaction,
} from "wagmi";
import { commitRevealABI } from "../config/abis/commitReveal";
import { getContract } from "../config/contracts";
import { TransactionReceipt } from "viem";

interface MintProps {
  hash?: BytesLike;
  onMintSuccess: (txHash?: string, tokenId?: BigNumberish) => void;
  closed: boolean;
}

interface WagmiError {
  reason?: string;
}

const EMPTY_HASH =
  "0xc5d2460186f7233c927e7db2dcc703c0e500b653ca82273b7bfad8045d85a470";

function Mint({ hash, onMintSuccess, closed }: MintProps) {
  const { isConnected } = useAccount();
  const { chain } = useNetwork();
  const [success, setSuccess] = useState<boolean>();

  const commitmentHash = hash as `0x${string}`;
  const { config } = usePrepareContractWrite({
    address: getContract(chain),
    abi: commitRevealABI,
    functionName: "commit",
    args: commitmentHash && [commitmentHash],
  });
  const {
    write: mint,
    data: txData,
    error: writeError,
  } = useContractWrite(config);
  const { error: mintError, isLoading: isMinting } = useWaitForTransaction({
    hash: txData?.hash,
    onSuccess(data) {
      setSuccess(true);
      onMintSuccess(txData?.hash, parseTokenId(data));
    },
  });

  const enabled = !closed && isConnected && hash && hash !== EMPTY_HASH;
  const error = (mintError || writeError) as WagmiError;

  const parseTokenId = (data: TransactionReceipt) => {
    const log = data.logs
      .map((log) => {
        try {
          const contract = new Interface(commitRevealABI);
          const parsed = contract.parseLog(log);
          return parsed;
        } catch {
          return;
        }
      })
      .find((log) => log?.name == "Transfer");
    return log?.args.tokenId;
  };

  const onClick = () => {
    if (enabled && !isMinting && !success && mint) {
      mint();
    }
  };

  const getMessage = () => {
    if (error) {
      const reason = error?.reason;
      return reason ? `Error: ${reason}` : "Error";
    }
    if (success) return "Success!";
    if (closed) return "Minting closed";
    if (!enabled) return "Type to mint";
    return "Mint this commitment";
  };

  const message = getMessage();

  return (
    <div>
      <button
        className="bg-red-600 disabled:bg-neutral-400 font-2xl text-white shadow-lg rounded-xl font-bold px-4 py-2 cursor-pointer transform transition duration-250 hover:scale-[102.5%]"
        onClick={onClick}
        disabled={!enabled}
      >
        {isMinting ? "Minting..." : message}
      </button>
    </div>
  );
}

export default Mint;
