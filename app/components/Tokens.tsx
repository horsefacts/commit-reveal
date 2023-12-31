import { useAccount, useNetwork, usePublicClient } from "wagmi";
import { commitRevealABI } from "../config/abis/commitReveal";
import { getContract } from "../config/contracts";
import { Hex } from "viem";
import { useCallback, useEffect, useState } from "react";
import { getColor } from "../utils";

interface TokensProps {
  onTokenSelected: (token: Token) => void;
}

export interface Token {
  tokenId: number;
  tokenURI: string;
  commitmentHash: Hex;
  commitment: string;
  metadata: {
    name: string;
    description: string;
    image: string;
  };
}

function Tokens({ onTokenSelected }: TokensProps) {
  const { chain } = useNetwork();
  const { address, isConnected } = useAccount();
  const contract = getContract(chain);
  const publicClient = usePublicClient();

  const [tokens, setTokens] = useState<Token[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const [selectedToken, setSelectedToken] = useState<number>();

  const getTokensofOwner = useCallback(async () => {
    setIsLoading(true);
    const sent = await publicClient.getContractEvents({
      address: contract,
      abi: commitRevealABI,
      eventName: "Transfer",
      args: {
        sender: address,
      },
      fromBlock: "earliest",
      toBlock: "latest",
    });
    const received = await publicClient.getContractEvents({
      address: contract,
      abi: commitRevealABI,
      eventName: "Transfer",
      args: {
        receiver: address,
      },
      fromBlock: "earliest",
      toBlock: "latest",
    });
    const logs = sent
      .concat(received)
      .sort(
        (a, b) =>
          Number(a.blockNumber - b.blockNumber) ||
          a.transactionIndex - b.transactionIndex,
      );
    const owned = new Set<bigint>();
    for (const log of logs) {
      const { sender, receiver, tokenId } = log.args;
      if (sender === address && tokenId) {
        owned.delete(tokenId);
      } else if (receiver === address && tokenId) {
        owned.add(tokenId);
      }
    }
    let tokenData: Token[] = [];
    for (const tokenId of owned) {
      const tokenURI = await publicClient.readContract({
        address: contract,
        abi: commitRevealABI,
        functionName: "tokenURI",
        args: [tokenId],
      });
      const commitment = await publicClient.readContract({
        address: contract,
        abi: commitRevealABI,
        functionName: "commitments",
        args: [tokenId],
      });
      const commitmentHash = await publicClient.readContract({
        address: contract,
        abi: commitRevealABI,
        functionName: "commitmentHashes",
        args: [tokenId],
      });
      const metadata = JSON.parse(
        Buffer.from(tokenURI.split(",")[1], "base64").toString(),
      );
      tokenData.push({
        tokenId: Number(tokenId),
        tokenURI,
        commitmentHash,
        commitment,
        metadata,
      });
    }
    setTokens(tokenData);
    setIsLoading(false);
  }, [publicClient, contract, address]);

  useEffect(() => {
    getTokensofOwner();
  }, [getTokensofOwner]);

  const truncate = (hash: Hex) => {
    return hash.slice(0, 6) + "…" + hash.slice(-4);
  };

  return (
    <div>
      {isConnected && isLoading && <div>Looking up your commitments...</div>}
      {isConnected && !isLoading && (
        <div>
          <div>Select a commitment:</div>
          <div className="flex flex-row flex-wrap">
            {tokens.map((token) => (
              <div
                key={token.tokenId}
                className="mr-4 cursor-pointer"
                onClick={() => {
                  setSelectedToken(token.tokenId);
                  onTokenSelected(token);
                }}
              >
                <span
                  className={`text-${getColor(token.tokenId)}-500 ${
                    token.tokenId === selectedToken ? "underline" : ""
                  }`}
                >
                  <code className="text-lg">
                    {truncate(token.commitmentHash)}
                  </code>
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
      {isConnected && !isLoading && tokens.length === 0 && (
        <div className="py-2">You don&apos;t own any Commit/Reveal tokens.</div>
      )}
    </div>
  );
}

export default Tokens;
