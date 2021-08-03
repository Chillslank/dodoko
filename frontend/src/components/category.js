import React from 'react'
import styled from 'styled-components'
import { Tabs } from 'antd';

const { TabPane } = Tabs;

function callback(key) {
  console.log(key);
}

export function Category(props) {
  return (
    <CategoryWrapper>
      <CategoryTitleWrapper>
        Action
      </CategoryTitleWrapper>
      <Tabs defaultActiveKey="1" onChange={callback}>
        <TabPane tab="What's Popular" key="1">
          <GamesList />
        </TabPane>
        <TabPane tab="Top Rated" key="2">
          <GamesList />
        </TabPane>
      </Tabs>
    </CategoryWrapper>
  )
}

function GamesList(props) {
  

  return (
    <div>

    </div>
  )
}

const CategoryWrapper = styled.div`
  width: 800px;
  margin: 0 auto;
`
const CategoryTitleWrapper = styled.h1`
  height: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
`
