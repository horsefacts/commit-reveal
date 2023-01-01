import { BigNumber } from "ethers";
import Image from "next/image";
import { useEffect, useState } from "react";
import Confetti from "react-dom-confetti";
import { useNetwork } from "wagmi";

import { useMetadata } from "../hooks/contracts";

interface SuccessProps {
  txHash?: string;
  tokenId?: BigNumber;
}

function Success({ txHash, tokenId }: SuccessProps) {
  const { chain } = useNetwork();
  const { tokenMetadata } = useMetadata(tokenId);
  const [active, setActive] = useState<boolean>(false);

  useEffect(() => {
    setActive(true);
  }, []);

  const etherscanURL =
    chain && `${chain.blockExplorers?.default.url}/tx/${txHash}`;

  return (
    <div>
      <div className="flex flex-row place-items-center">
        <div className="py-8 text-center">
          {tokenMetadata && (
            <Image
              alt="Commitment"
              src={tokenMetadata.image}
              width={1400}
              height={600}
              className="rounded-md"
            />
          )}
          <div className="font-bold text-red-500">
            Your commitment was minted.
          </div>
          {etherscanURL && (
            <p>
              <a
                className="underline cursor-pointer text-neutral-600 hover:text-red-500"
                href={etherscanURL}
                target="_blank"
                rel="noreferrer"
              >
                View on Etherscan
              </a>
            </p>
          )}
          <div className="mx-auto">
            <Confetti
              active={active}
              config={{
                angle: 90,
                spread: 420,
                elementCount: 100,
                duration: 3500,
                width: "10px",
                height: "10px",
              }}
            />
          </div>
        </div>
      </div>
    </div>
  );
}

export default Success;
