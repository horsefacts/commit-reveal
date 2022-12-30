import ape

ZERO_ADDRESS = '0x0000000000000000000000000000000000000000'

def test_owner_set_on_initialization(cr, owner):
    assert cr.owner() == owner

def test_token_has_name(cr):
    assert cr.name() ==  "Commit/Reveal"

def test_token_has_symbol(cr):
    assert cr.symbol() ==  "C/R 2022"

def test_balance_of(cr, owner, receiver):
    cr.mint(receiver, 1, sender=owner)
    assert cr.balanceOf(receiver) == 1

def test_balance_of_reverts_zero_address(cr):
    with ape.reverts("Zero address"):
        cr.balanceOf(ZERO_ADDRESS)

def test_owner_of(cr, owner, receiver):
    cr.mint(receiver, 1, sender=owner)
    assert cr.ownerOf(1) == receiver

def test_owner_of_reverts_not_minted(cr):
    with ape.reverts("Not minted"):
        cr.ownerOf(1)

def test_mint_reverts_zero_address(cr, owner):
    with ape.reverts("Invalid receiver"):
        cr.mint(ZERO_ADDRESS, 1, sender=owner)

def test_mint_reverts_already_minted(cr, owner, receiver):
    cr.mint(receiver, 1, sender=owner)
    with ape.reverts("Already minted"):
        cr.mint(receiver, 1, sender=owner)

def test_mint_emits_transfer_event(cr, owner, receiver):
    tx = cr.mint(receiver, 1, sender=owner)
    logs = list(tx.decode_logs(cr.Transfer))
    assert len(logs) == 1
    assert logs[0].sender == ZERO_ADDRESS
    assert logs[0].receiver == receiver
    assert logs[0].tokenId == 1

def test_transfer_reverts_wrong_owner(cr, owner, receiver, other):
    cr.mint(receiver, 1, sender=owner)
    with ape.reverts("Wrong owner"):
        cr.transferFrom(other, other, 1, sender=other)

def test_transfer_reverts_zero_receiver(cr, owner, receiver, other):
    cr.mint(receiver, 1, sender=owner)
    with ape.reverts("Invalid receiver"):
        cr.transferFrom(receiver, ZERO_ADDRESS, 1, sender=other)

def test_transfer_reverts_not_approved(cr, owner, receiver, other):
    cr.mint(receiver, 1, sender=owner)
    with ape.reverts("Not approved"):
        cr.transferFrom(receiver, other, 1, sender=other)

def test_transfer_updates_balances(cr, owner, receiver, other):
    cr.mint(receiver, 1, sender=owner)
    cr.transferFrom(receiver, other, 1, sender=receiver)
    assert cr.balanceOf(receiver) == 0
    assert cr.balanceOf(other) == 1

def test_transfer_updates_ownership(cr, owner, receiver, other):
    cr.mint(receiver, 1, sender=owner)
    cr.transferFrom(receiver, other, 1, sender=receiver)
    assert cr.ownerOf(1) == other

def test_approved_transfer(cr, owner, receiver, other, operator):
    cr.mint(receiver, 1, sender=owner)
    cr.approve(operator, 1, sender=receiver)
    cr.transferFrom(receiver, other, 1, sender=operator)
    assert cr.ownerOf(1) == other

def test_approved_all_transfer(cr, owner, receiver, other, operator):
    cr.mint(receiver, 1, sender=owner)
    cr.setApprovalForAll(operator, True, sender=receiver)
    cr.transferFrom(receiver, other, 1, sender=operator)
    assert cr.ownerOf(1) == other

def test_transfer_clears_approval(cr, owner, receiver, other, operator):
    cr.mint(receiver, 1, sender=owner)
    cr.approve(operator, 1, sender=receiver)
    assert cr.getApproved(1) == operator
    cr.transferFrom(receiver, other, 1, sender=receiver)
    assert cr.getApproved(1) == ZERO_ADDRESS

def test_transfer_emits_transfer_event(cr, owner, receiver, other):
    cr.mint(receiver, 1, sender=owner)
    tx = cr.transferFrom(receiver, other, 1, sender=receiver)
    logs = list(tx.decode_logs(cr.Transfer))
    assert len(logs) == 1
    assert logs[0].sender == receiver
    assert logs[0].receiver == other
    assert logs[0].tokenId == 1

def test_safe_transfer_reverts_unsafe_receiver(cr, owner, receiver, unsafe_receiver):
    cr.mint(receiver, 1, sender=owner)
    with ape.reverts("Unsafe receiver"):
        cr.safeTransferFrom(receiver, unsafe_receiver, 1, sender=receiver)

def test_safe_transfer_safe_receiver(cr, owner, receiver, safe_receiver):
    cr.mint(receiver, 1, sender=owner)
    cr.safeTransferFrom(receiver, safe_receiver, 1, sender=receiver)
    assert cr.ownerOf(1) == safe_receiver

def test_set_approval_for_all(cr, owner, operator):
    cr.setApprovalForAll(operator, True, sender=owner)
    assert cr.isApprovedForAll(owner, operator)

def test_set_approval_for_all_emits_event(cr, owner, operator):
    approve = cr.setApprovalForAll(operator, True, sender=owner)
    logs = list(approve.decode_logs(cr.ApprovalForAll))
    assert len(logs) == 1
    assert logs[0].owner == owner
    assert logs[0].operator == operator
    assert logs[0].isApproved == True

    revoke = cr.setApprovalForAll(operator, False, sender=owner)
    logs = list(revoke.decode_logs(cr.ApprovalForAll))
    assert len(logs) == 1
    assert logs[0].owner == owner
    assert logs[0].operator == operator
    assert logs[0].isApproved == False

def test_approve(cr, owner, receiver, other):
    cr.mint(receiver, 1, sender=owner)
    cr.approve(other, 1, sender=receiver)
    assert cr.getApproved(1) == other

def test_approve_approved_for_all(cr, owner, receiver, other, operator):
    cr.mint(receiver, 1, sender=owner)
    cr.setApprovalForAll(operator, True, sender=receiver)
    cr.approve(other, 1, sender=operator)
    assert cr.getApproved(1) == other

def test_approve_reverts_unapproved(cr, owner, receiver, other):
    cr.mint(receiver, 1, sender=owner)
    with ape.reverts("Not approved"):
        cr.approve(other, 1, sender=other)

def test_approve_emits_approval_event(cr, owner, receiver, other):
    cr.mint(receiver, 1, sender=owner)
    tx = cr.approve(other, 1, sender=receiver)
    logs = list(tx.decode_logs(cr.Approval))
    assert len(logs) == 1
    assert logs[0].owner == receiver
    assert logs[0].approved == other
    assert logs[0].tokenId == 1
