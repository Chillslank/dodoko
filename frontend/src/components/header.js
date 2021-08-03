import React from 'react'
import styled from 'styled-components'
export function Header() {
  return (
    <HeaderWrapper>
      <HeaderLeft>
        <HeaderItem>Logo</HeaderItem>
        <HeaderItem>Category</HeaderItem>
        <HeaderItem>Wish List</HeaderItem>
        <HeaderItem>About</HeaderItem>
      </HeaderLeft>      
      <HeaderRight>
        <HeaderRightItem>Log In</HeaderRightItem>
        <HeaderRightItem>Sign Up</HeaderRightItem>
      </HeaderRight>      
    </HeaderWrapper>
  )
}

const HeaderWrapper = styled.div`
height: 50px;
display: flex;
justify-content: space-between;
cursor: pointer;
margin-bottom: 50px;
`
const HeaderLeft = styled.div`
  width: 40%;
  display: flex;
  
`
const HeaderRight = styled.div`
  width: 20%;
  display: flex;
`
const HeaderItem = styled.div`
  width: 25%;
  display: flex;
  justify-content: center;
  align-items: center;
`
const HeaderRightItem = styled.div`
  width: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
`