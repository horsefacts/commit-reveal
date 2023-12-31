import Head from "next/head";
import { useState } from "react";

import About from "../components/About";
import Connect from "../components/Connect";
import ContractInfo from "../components/ContractInfo";
import Success from "../components/Success";
import { useHasMounted } from "../hooks/hasMounted";

import type { NextPage } from "next";
import Tokens, { Token } from "../components/Tokens";
import Reveal from "../components/Reveal";
const Home: NextPage = () => {
  const hasMounted = useHasMounted();
  const [token, setToken] = useState<Token>();
  const [txHash, setTxHash] = useState<string>();
  const [success, setSuccess] = useState<boolean>(false);

  const onRevealSuccess = (txHash: string) => {
    setTxHash(txHash);
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
              <Success txHash={txHash} tokenId={token?.tokenId} />
            ) : (
              <>
                <Tokens onTokenSelected={setToken} />
                {token && (
                  <Reveal token={token} onRevealSuccess={onRevealSuccess} />
                )}
                <About />
              </>
            )}
          </main>
        </div>
      )}
    </div>
  );
};

export default Home;
