import React from "react";

function About() {
  return (
    <div className="space-y-2 max-w-prose">
      <p>Connect your wallet and select a 2023 commitment to reveal.</p>
      <p>
        You&apos;ll need to enter the <strong>exact text</strong> of your
        commitment message in order to reveal it.
      </p>
      <div className="text-xs cursor-pointer text-neutral-400 hover:text-neutral-600">
        <a
          href="https://twitter.com/eth_call/status/1609463639399956482"
          target="_blank"
          rel="noreferrer"
          className="pt-16"
        >
          Created NYE 2022 by <pre className="inline">@eth_call</pre>
        </a>
      </div>
    </div>
  );
}

export default About;
