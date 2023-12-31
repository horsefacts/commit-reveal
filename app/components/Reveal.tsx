import { keccak256, toUtf8Bytes } from "ethers";
import React, { useState } from "react";
import { Token } from "./Tokens";
import {
  useAccount,
  useNetwork,
  usePrepareContractWrite,
  useContractWrite,
  useWaitForTransaction,
} from "wagmi";
import { commitRevealABI } from "../config/abis/commitReveal";
import { getContract } from "../config/contracts";
import { getColor } from "../utils";

interface RevealProps {
  token?: Token;
  onRevealSuccess: (txHash: string) => void;
}

interface WagmiError {
  reason?: string;
}

function Reveal({ token, onRevealSuccess }: RevealProps) {
  const { isConnected } = useAccount();
  const { chain } = useNetwork();
  const [success, setSuccess] = useState<boolean>();
  const [commitment, setCommitment] = useState("");

  const { config } = usePrepareContractWrite({
    address: getContract(chain),
    abi: commitRevealABI,
    functionName: "reveal",
    args: [BigInt(token?.tokenId || 0), commitment],
  });
  const {
    write: reveal,
    data: txData,
    error: writeError,
  } = useContractWrite(config);
  const { error: revealError, isLoading } = useWaitForTransaction({
    hash: txData?.hash,
    onSuccess() {
      setSuccess(true);
      onRevealSuccess(txData?.hash ?? "");
    },
  });

  const hash = keccak256(toUtf8Bytes(commitment));
  const matchingHash = hash === token?.commitmentHash;
  const alreadyRevealed = token?.commitment !== "";
  const canReveal = isConnected && commitment && !alreadyRevealed;
  const enabled = canReveal && matchingHash;
  const error = (revealError || writeError) as WagmiError;

  function handleChange(event: React.ChangeEvent<HTMLTextAreaElement>) {
    if (event.target.value.length <= 256) {
      setCommitment(event.target.value);
    }
  }

  const onClick = () => {
    if (enabled && !isLoading && !success && reveal) {
      reveal();
    }
  };

  const getMessage = () => {
    if (error) {
      const reason = error?.reason;
      return reason ? `Error: ${reason}` : "Error";
    }
    if (success) return "Success!";
    if (!enabled) return "Type to reveal";
    return "Click to reveal";
  };

  const message = getMessage();

  if (!isConnected) return <div></div>;
  return (
    <div>
      {alreadyRevealed ? (
        <div>
          <div
            className="relative md:w-[700px] h-[300px] rounded-lg overflow-hidden"
            style={{ backgroundImage: `url(${token?.metadata.image})` }}
          ></div>
        </div>
      ) : (
        <div>
          <div className="relative w-[700px] h-[300px] rounded-lg overflow-hidden">
            <textarea
              style={{ backgroundImage: `url(${token?.metadata.image})` }}
              className="w-[700px] font-mono bg-dark text-white text-xl pt-16 pb-32 px-8"
              value={commitment}
              onChange={handleChange}
              rows={6}
              cols={50}
              placeholder="Type your commitment here…"
            />
            <div
              className="absolute bottom-6 right-6 w-[700px] font-mono flex flex-row flex-wrap justify-between px-2 md:flex-row-reverse
        md:pb-0 pb-2"
            >
              <div
                className={`truncate ${
                  hash === token?.commitmentHash
                    ? `text-${getColor(token?.tokenId)}-500`
                    : "text-gray-400"
                }`}
              >
                {hash}
              </div>
            </div>
          </div>
          <div className="py-4">
            <button
              className="bg-red-600 disabled:bg-neutral-400 font-2xl text-white shadow-lg rounded-xl font-bold px-4 py-2 cursor-pointer transform transition duration-250 hover:scale-[102.5%]"
              onClick={onClick}
              disabled={!enabled}
            >
              {isLoading ? "Revealing..." : message}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Reveal;
