import React from 'react';
import TimeAgo from 'react-timeago';

function About() {
  return (
    <div className="space-y-2 max-w-prose">
      <p>
        Type a message in the box above to create a hashed onchain commitment.
        You&apos;ll receive a token representing your commitment that can be
        revealed on New Year&apos;s Eve 2023 (or later). Use this to make a
        prediction or resolution today and reveal it a year from now.
      </p>
      <p>
        You&apos;ll need the <strong>exact text</strong> of your commitment
        message in order to reveal it in December, so make sure you save it
        somewhere safe.
      </p>
      <p>
        A longer commitment message will cost more gas to reveal later, so you
        may want to keep it short.
      </p>
      <p>
        Tokens are free and unlimited, but can only be minted for a week.
        Commitments will close{" "}
        <TimeAgo date={new Date(1673136000 * 1000)} className="font-bold" />.
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
