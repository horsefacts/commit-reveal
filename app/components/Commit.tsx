import { BytesLike, keccak256, toUtf8Bytes } from "ethers/lib/utils.js";
import Image from "next/image";
import React, { useState } from "react";

interface UploadProps {
  onCommitmentChange: (hash: BytesLike) => void;
}

function Upload({ onCommitmentChange }: UploadProps) {
  const [commitment, setCommitment] = useState("");

  function handleChange(event: React.ChangeEvent<HTMLTextAreaElement>) {
    if (event.target.value.length <= 256) {
      setCommitment(event.target.value);
      onCommitmentChange(keccak256(toUtf8Bytes(event.target.value)));
    }
  }

  return (
    <div className="relative">
      <textarea
        className="w-full font-mono rounded-lg bg-dark text-white text-xl pt-16 pb-32 px-8"
        value={commitment}
        onChange={handleChange}
        rows={6}
        cols={50}
        placeholder="Type your commitment here…"
      />
      <div
        className="absolute bottom-4 w-full font-mono text-red-500 flex flex-row flex-wrap justify-between px-2 md:flex-row-reverse
        md:pb-0 pb-2"
      >
        <div>{toUtf8Bytes(commitment).length}/256 bytes</div>
        <div className="truncate">{keccak256(toUtf8Bytes(commitment))}</div>
      </div>
    </div>
  );
}

export default Upload;
