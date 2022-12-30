# @version 0.3.7

from vyper.interfaces import ERC165
from vyper.interfaces import ERC721

implements: ERC165
implements: ERC721

interface ERC721TokenReceiver:
  def onERC721Received(
    operator: address,
    owner: address,
    tokenId: uint256,
    data: Bytes[1024]
  ) -> bytes4: view

event Transfer:
  sender: indexed(address)
  receiver: indexed(address)
  tokenId: indexed(uint256)

event Approval:
  owner: indexed(address)
  approved: indexed(address)
  tokenId: indexed(uint256)

event ApprovalForAll:
  owner: indexed(address)
  operator: indexed(address)
  isApproved: bool

SUPPORTED_INTERFACE_IDS: constant(bytes4[3]) = [
    0x01ffc9a7,  # ERC165
    0x80ac58cd,  # ERC721
    0x5b5e139f   # ERC721 Metadata
]

NAME: constant(String[13]) = "Commit/Reveal"
SYMBOL: constant(String[8]) = "C/R 2022"

owner: public(address)

_ownerOf: HashMap[uint256, address]
_balanceOf: HashMap[address, uint256]

getApproved: public(HashMap[uint256, address])
isApprovedForAll: public(HashMap[address, HashMap[address, bool]])

@external
def __init__():
    self.owner = msg.sender

@pure
@external
def supportsInterface(interface_id: bytes4) -> bool:
    return interface_id in SUPPORTED_INTERFACE_IDS

@pure
@external
def name() -> String[13]:
    return NAME

@pure
@external
def symbol() -> String[8]:
    return SYMBOL

@view
@external
def ownerOf(tokenId: uint256) -> address:
    tokenOwner: address = self._ownerOf[tokenId]
    assert tokenOwner != empty(address), "Not minted"
    return  tokenOwner

@view
@external
def balanceOf(owner: address) -> uint256:
    assert owner != empty(address), "Zero address"
    return self._balanceOf[owner]

@external
def mint(receiver: address, tokenId: uint256):
    self._mint(receiver, tokenId)

@external
def approve(spender: address, tokenId: uint256):
    tokenOwner: address = self._ownerOf[tokenId]
    assert msg.sender == tokenOwner or self.isApprovedForAll[tokenOwner][msg.sender], "Not approved"

    self.getApproved[tokenId] = spender

    log Approval(tokenOwner, spender, tokenId)

@external
def setApprovalForAll(operator: address, approved: bool):
    self.isApprovedForAll[msg.sender][operator] = approved

    log ApprovalForAll(msg.sender, operator, approved)

@external
def transferFrom(owner: address, receiver: address, tokenId: uint256):
    self._transferFrom(owner, receiver, tokenId)

@external
def safeTransferFrom(owner: address, receiver: address, tokenId: uint256, data: Bytes[1024]=b""):
    self._transferFrom(owner, receiver, tokenId)
    if receiver.is_contract:
        returnValue: bytes4 = ERC721TokenReceiver(receiver).onERC721Received(msg.sender, owner, tokenId, data)
        assert returnValue == method_id("onERC721Received(address,address,uint256,bytes)", output_type=bytes4), "Unsafe receiver"

@internal
def _transferFrom(owner: address, receiver: address, tokenId: uint256):
    assert owner == self._ownerOf[tokenId], "Wrong owner"
    assert receiver != empty(address), "Invalid receiver"
    assert msg.sender == owner or self.isApprovedForAll[owner][msg.sender] or msg.sender == self.getApproved[tokenId], "Not approved"

    self._balanceOf[owner] -= 1
    self._balanceOf[receiver] += 1
    self._ownerOf[tokenId] = receiver

    self.getApproved[tokenId] = empty(address)

    log Transfer(owner, receiver, tokenId)

@internal
def _mint(receiver: address, tokenId: uint256):
    assert receiver != empty(address), "Invalid receiver"
    assert self._ownerOf[tokenId] == empty(address), "Already minted"

    self._balanceOf[receiver] += 1
    self._ownerOf[tokenId] = receiver

    log Transfer(empty(address), receiver, tokenId)
