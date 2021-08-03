import React from 'react'
import styled from 'styled-components'

export function Categories() {
  return (
    <CategoriesWrapper>
      <Category />
      <Category />
      <Category />
      <Category />
      <Category />
      <Category />
      <Category />
      <Category />
      <Category />
    </CategoriesWrapper>
  )
}

function Category(props) {
  return (
    <CategoryWrapper>
      
    </CategoryWrapper>
  )
}

const CategoriesWrapper = styled.div`
  width: 60%;
  display: flex;
  flex-wrap: wrap;
  margin: 0 auto;
  justify-content: space-around;
  align-items: center;
`

const CategoryWrapper = styled.div`
  width: 30%;
  height: 200px;
  margin-bottom: 30px;
  
  &:hover {
    box-shadow:0 0 10px #ccc;
  }
`