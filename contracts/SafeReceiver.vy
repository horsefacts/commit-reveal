# @version 0.3.7

implements: ERC721TokenReceiver


interface ERC721TokenReceiver:
    def onERC721Received(
        operator: address, owner: address, tokenId: uint256, data: Bytes[1024]
    ) -> bytes4:
        view


@view
@external
def onERC721Received(
    operator: address, owner: address, tokenId: uint256, data: Bytes[1024]
) -> bytes4:
    return method_id(
        "onERC721Received(address,address,uint256,bytes)", output_type=bytes4
    )
