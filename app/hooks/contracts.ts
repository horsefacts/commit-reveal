import { BigNumberish } from "ethers";
import { useContractRead, useNetwork } from "wagmi";

import { commitRevealABI } from "../config/abis/commitReveal";
import { getContract } from "../config/contracts";

export function useMetadata(tokenId?: BigNumberish) {
  const { chain } = useNetwork();
  const { data, isError, isLoading } = useContractRead({
    address: getContract(chain),
    abi: commitRevealABI,
    functionName: "tokenURI",
    args: [BigInt(tokenId ?? 0)],
  });
  let tokenMetadata;
  if (data) {
    const json = Buffer.from(data.substring(29), "base64").toString();
    tokenMetadata = JSON.parse(json);
  }
  return { data, tokenMetadata, isError, isLoading };
}
