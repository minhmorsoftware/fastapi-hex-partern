import pytest

from todolist.core.todo.services.todo_item_service import (
    create_one,
    delete_many,
    delete_one,
    get_all,
    get_one,
    update_many,
    update_one,
)

# Consts
PERSIST_ONE_FN_NAME = "persist_one_fn"
DELETE_MANY_FN_NAME = "delete_many_fn"
DELETE_ONE_FN_NAME = "delete_one_fn"
FETCH_ALL_FN_NAME = "fetch_all_fn"
FETCH_ONE_FN_NAME = "fetch_one_fn"
UPDATE_MANY_FN_NAME = "update_many_fn"
UPDATE_ONE_FN_NAME = "update_one_fn"


@pytest.fixture(name=PERSIST_ONE_FN_NAME)
def persist_one_fn_fixture(repo_fn_factory):
    return repo_fn_factory(PERSIST_ONE_FN_NAME)


@pytest.fixture(name=DELETE_MANY_FN_NAME)
def delete_many_fn_fixture(repo_fn_factory):
    return repo_fn_factory(DELETE_MANY_FN_NAME)


@pytest.fixture(name=DELETE_ONE_FN_NAME)
def delete_one_fn_fixture(repo_fn_factory):
    return repo_fn_factory(DELETE_ONE_FN_NAME)


@pytest.fixture(name=FETCH_ALL_FN_NAME)
def fetch_all_fn_fixture(repo_fn_factory):
    return repo_fn_factory(FETCH_ALL_FN_NAME)


@pytest.fixture(name=FETCH_ONE_FN_NAME)
def fetch_one_fn_fixture(repo_fn_factory):
    return repo_fn_factory(FETCH_ONE_FN_NAME)


@pytest.fixture(name=UPDATE_MANY_FN_NAME)
def update_many_fn_fixture(repo_fn_factory):
    return repo_fn_factory(UPDATE_MANY_FN_NAME)


@pytest.fixture(name=UPDATE_ONE_FN_NAME)
def update_one_fn_fixture(repo_fn_factory):
    return repo_fn_factory(UPDATE_ONE_FN_NAME)


# Tests
@pytest.mark.unit
@pytest.mark.asyncio
async def test_create_one(
    persist_one_fn, user_registry, create_todo_item_dto, todo_item
):
    # Setup
    persist_one_fn.return_value.set_result(todo_item)

    # Test
    result = await create_one(persist_one_fn, user_registry, create_todo_item_dto)

    # Assertions
    persist_one_fn.assert_called_once_with(user_registry, create_todo_item_dto)
    assert result == todo_item


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete_many(delete_many_fn, user_registry):
    # Setup
    ids = range(1, 6)
    delete_many_fn.return_value.set_result(True)

    # Test
    result = await delete_many(delete_many_fn, user_registry, ids)

    #  Assertions
    delete_many_fn.assert_called_once_with(user_registry, ids)
    assert result is True


@pytest.mark.unit
@pytest.mark.asyncio
async def test_delete_one(delete_one_fn, user_registry):
    # Setup
    id_ = 1
    delete_one_fn.return_value.set_result(True)

    # Tests
    result = await delete_one(delete_one_fn, user_registry, id_)

    # Assertions
    delete_one_fn.assert_called_once_with(user_registry, id_)
    assert result is True


@pytest.mark.unit
@pytest.mark.asyncio
async def test_get_all(fetch_all_fn, user_registry, todo_items):
    # Setup
    items = todo_items()
    fetch_all_fn.return_value.set_result(items)

    # Tests
    result = await get_all(fetch_all_fn, user_registry)

    # Assertions
    fetch_all_fn.assert_called_once_with(user_registry)
    assert result == items


@pytest.mark.unit
@pytest.mark.asyncio
async def test_fetch_one(fetch_one_fn, user_registry, todo_item):
    # Setup
    id_ = todo_item.id
    fetch_one_fn.return_value.set_result(todo_item)

    # Tests
    result = await get_one(fetch_one_fn, user_registry, id_)

    # Assertions
    fetch_one_fn.assert_called_once_with(user_registry, id_)
    assert result == todo_item


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_many(
    update_many_fn, user_registry, update_todo_item_dtos, todo_items
):
    # Setup
    dtos = update_todo_item_dtos()
    ids = range(1, len(dtos) + 1)
    items = todo_items()
    update_many_fn.return_value.set_result(items)

    # Tests
    result = await update_many(update_many_fn, user_registry, dtos, ids)

    # Assertions
    update_many_fn.assert_called_once()
    assert result == items


@pytest.mark.unit
@pytest.mark.asyncio
async def test_update_one(
    update_one_fn, user_registry, update_todo_item_dto, todo_item
):
    # Setup
    id_ = 1
    update_one_fn.return_value.set_result(todo_item)

    # Tests
    result = await update_one(update_one_fn, user_registry, update_todo_item_dto, id_)

    # Assertions
    update_one_fn.assert_called_once_with(user_registry, update_todo_item_dto, id_)
    assert result == todo_item
