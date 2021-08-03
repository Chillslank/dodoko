import React from 'react'
import styled from 'styled-components'
import { Table, Space, Button } from 'antd';
export function Wishlist() {
  return (
    <Wrapper>
      <h1>Wish List</h1>
      <GameListItem />
    </Wrapper>
  )
}

const GameListItem = function() {

  const data = [
    {name: "Pubg"}
  ]

  return (
    
      <Table dataSource={data} showHeader={false} pagination={false}> 
        <Table.Column title="Game Name" dataIndex="name" key="name" />
        <Table.Column align={"right"}
          title="Action"
          key="action"
          render={() => (
            <Space size="middle">
              <Button type="link">
                Delete 
              </Button>
            </Space>
          )}
        />
      </Table>
    
  )

}



const Wrapper = styled.div`
  width: 600px;
  margin: 0 auto;
  
`