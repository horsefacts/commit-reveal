import { mainnet } from "wagmi";
import { goerli } from "wagmi/chains";

import { Chain } from "@rainbow-me/rainbowkit";
import { Hex } from "viem";

const contracts: { [chainId: number]: Hex } = {
  [goerli.id]: "0x5Ea382b48b91778F21D1e605D395579EA3a93638",
  [mainnet.id]: "0x71c54ad9f410ed85e81e38af9efc08bac3968665",
};

export function getContract(currentChain?: Chain): Hex {
  return currentChain ? contracts[currentChain.id] : contracts[goerli.id];
}
