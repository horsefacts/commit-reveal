import pytest


@pytest.fixture(scope="session")
def owner(accounts):
    return accounts[0]

@pytest.fixture(scope="session")
def receiver(accounts):
    return accounts[1]

@pytest.fixture(scope="session")
def other(accounts):
    return accounts[2]

@pytest.fixture(scope="session")
def operator(accounts):
    return accounts[3]

@pytest.fixture(scope="session")
def metadata(owner, project):
    return owner.deploy(project.Metadata)

@pytest.fixture(scope="session")
def cr(owner, project, metadata):
    return owner.deploy(project.CommitRevealMintable, metadata)

@pytest.fixture(scope="session")
def unsafe_receiver(owner, project):
    return owner.deploy(project.UnsafeReceiver)

@pytest.fixture(scope="session")
def safe_receiver(owner, project):
    return owner.deploy(project.SafeReceiver)

@pytest.fixture(scope="session")
def b64(owner, project):
    return owner.deploy(project.Base64)
