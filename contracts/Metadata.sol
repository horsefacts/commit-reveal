// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/access/Ownable.sol";
import "@openzeppelin/utils/Strings.sol";
import "@openzeppelin/utils/Base64.sol";

interface ICommitReveal {
  function commitmentHashes(uint256 tokenID) external view returns (bytes32);

  function commitments(uint256 tokenID) external view returns (string memory);
}

contract Metadata is Ownable {
  using Strings for uint256;

  ICommitReveal public token;

  string[6] colors = [
    "ef4444",
    "f97316",
    "eab308",
    "22c55e",
    "0ea5e9",
    "8b5cf6"
  ];

  function contractURI() external view returns (string memory) {
    return
      _dataURI(
        "application/json",
        '{"name":"Commit/Reveal 2023","description":"Hashed onchain commitments, revealable December 31, 2023"}'
      );
  }

  function tokenURI(uint256 tokenId) external view returns (string memory) {
    return _dataURI("application/json", tokenJSON(tokenId));
  }

  function tokenJSON(uint256 tokenId) public view returns (string memory) {
    return
      string.concat(
        '{"name":"',
        _commitmentHash(tokenId),
        '","description":"This token represents a hashed commitment that can be revealed December 31, 2023.","image":"',
        _dataURI("image/svg+xml", tokenSVG(tokenId)),
        '"}'
      );
  }

  function tokenSVG(uint256 tokenId) public view returns (string memory) {
    return
      string.concat(
        '<svg xmlns="http://www.w3.org/2000/svg" style="background:#151520" viewBox="0 0 700 300"><path id="a" fill="#151520" d="M10 10h670a20 10 0 0 1 10 10v260a20 10 0 0 1-10 10H20a20 10 0 0 1-10-10V10z"/><text fill="#',
        _color(tokenId),
        '" dominant-baseline="middle" font-family="Menlo,monospace" font-size="12"><textPath href="#a">&#160;Commit/Reveal 2023 &#8226;<![CDATA[ ',
        _commitmentHashes(tokenId),
        ']]></textPath></text><path fill="rgba(0,0,0,0)" stroke="#',
        _color(tokenId),
        '" d="M20 20h650a10 10 0 0 1 10 10v240a10 10 0 0 1-10 10H30a10 10 0 0 1-10-10V20z"/><foreignObject x="50" y="30" width="620" height="250"><div style="font-family:Menlo,monospace;color:#fff;font-size:24px;display:flex;align-items:center;justify-content:center;height:240px"  xmlns="http://www.w3.org/1999/xhtml"><p>',
        _commitment(tokenId),
        "</p></div></foreignObject></svg>"
      );
  }

  function setToken(ICommitReveal _token) external onlyOwner {
    if (address(token) == address(0)) token = _token;
  }

  function _color(uint256 tokenId) internal view returns (string memory) {
    return colors[tokenId % colors.length];
  }

  function _commitmentHash(
    uint256 tokenId
  ) internal view returns (string memory) {
    return uint256(token.commitmentHashes(tokenId)).toHexString();
  }

  function _commitmentHashes(
    uint256 tokenId
  ) internal view returns (string memory) {
    string memory commitmentHash = _commitmentHash(tokenId);
    return
      string.concat(
        commitmentHash,
        " ",
        commitmentHash,
        " ",
        commitmentHash,
        " ",
        commitmentHash
      );
  }

  function _commitment(uint256 tokenId) internal view returns (string memory) {
    return token.commitments(tokenId);
  }

  function _dataURI(
    string memory mimeType,
    string memory data
  ) internal view returns (string memory) {
    return
      string.concat(
        "data:",
        mimeType,
        ";base64,",
        Base64.encode(abi.encodePacked(data))
      );
  }
}
