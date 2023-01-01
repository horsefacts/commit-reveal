import React from "react";
import TimeAgo from "react-timeago";

function About() {
  return (
    <div className="space-y-2 lg:w-2/3 md:w-3/4">
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
        A longer commitment message will cost more gas to reveal, so you may
        want to keep it short.
      </p>
      <p>
        Tokens are free and unlimited, but can only be minted for a week.
        Commitments will close{" "}
        <TimeAgo date={new Date(1673136000 * 1000)} className="font-bold" />.
      </p>
    </div>
  );
}

export default About;
