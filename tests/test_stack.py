import pytest
from Stack import Stack

def test_Stack():
    st = Stack()
    assert st.is_empty()
    assert st.size() == 0
    st.push(1)
    st.push(2)
    assert st.size() == 2
    assert st.peek() == 2
    st.push(3)
    assert st.peek() == 3
    assert st.pop()  == 3
    assert st.peek() == 2
    assert not st.is_empty()
    assert st.size() == 2