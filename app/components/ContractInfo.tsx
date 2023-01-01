import { useNetwork } from "wagmi";

import { getContract } from "../config/contracts";

function ContractInfo() {
  const { chain } = useNetwork();
  const contract = getContract(chain);

  const etherscanURL =
    chain && `${chain.blockExplorers?.default.url}/address/${contract}`;

  return (
    <div className="text-sm tracking-tighter text-neutral-400">
      {etherscanURL && (
        <span>
          <a
            className="cursor-pointer hover:text-neutral-600"
            href={etherscanURL}
            target="_blank"
            rel="noreferrer"
          >
            <pre className="inline text-xs">{contract}</pre>
          </a>
        </span>
      )}
    </div>
  );
}

export default ContractInfo;
