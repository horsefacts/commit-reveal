import { goerli, mainnet } from "wagmi";

import { Chain } from "@rainbow-me/rainbowkit";

const contracts = {
  [goerli.id]: "0x5Ea382b48b91778F21D1e605D395579EA3a93638",
  [mainnet.id]: "0x71c54ad9f410ed85e81e38af9efc08bac3968665",
};

export function getContract(currentChain?: Chain) {
  return currentChain ? contracts[currentChain.id] : contracts[goerli.id];
}
