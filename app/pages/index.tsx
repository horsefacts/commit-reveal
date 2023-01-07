import { BigNumber, BytesLike } from 'ethers';
import Head from 'next/head';
import { useState } from 'react';

import About from '../components/About';
import Commit from '../components/Commit';
import Connect from '../components/Connect';
import ContractInfo from '../components/ContractInfo';
import Mint from '../components/Mint';
import Success from '../components/Success';
import { useHasMounted } from '../hooks/hasMounted';

import type { NextPage } from "next";
const Home: NextPage = () => {
  const hasMounted = useHasMounted();
  const [hash, setHash] = useState<BytesLike>();
  const [txHash, setTxHash] = useState<string>();
  const [tokenId, setTokenId] = useState<BigNumber>();
  const [success, setSuccess] = useState<boolean>(false);

  const now = new Date();
  const close = new Date(1673136000 * 1000);
  const closed = now >= close;

  const onCommitmentChange = (hash: BytesLike) => {
    setHash(hash);
  };

  const onMintSuccess = (txHash?: string, tokenId?: BigNumber) => {
    setTxHash(txHash);
    setTokenId(tokenId);
    setSuccess(true);
  };

  return (
    <div>
      {hasMounted && (
        <div>
          <Head>
            <title>Commit/Reveal 2023</title>
            <link rel="shortcut icon" href="/favicon.svg" />
          </Head>
          <main className="max-w-screen-xl p-16 mx-auto space-y-4">
            <div>
              <h1 className="text-5xl font-bold tracking-tight text-red-500">
                Commit/Reveal
              </h1>
              <p className="italic tracking-tight">
                Hashed onchain commitments, revealable NYE 2023.
              </p>
              <ContractInfo />
            </div>
            <Connect />
            {success ? (
              <Success txHash={txHash} tokenId={tokenId} />
            ) : (
              <Commit onCommitmentChange={onCommitmentChange} />
            )}
            {!success && (
              <>
                <Mint
                  hash={hash}
                  onMintSuccess={onMintSuccess}
                  closed={closed}
                />
                <About now={now} close={close} />
              </>
            )}
          </main>
        </div>
      )}
    </div>
  );
};

export default Home;
