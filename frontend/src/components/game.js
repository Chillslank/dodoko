import React from 'react'
import styled from 'styled-components'
import { Button, Input, Rate } from 'antd';


export function Game() {
  return (
    <div>
      <GameDetailsWrapper>
        <h1>PUBG</h1>
        <p style={{fontSize: "18px"}}>PUBG: BATTLEGROUNDS is a battle royale shooter that pits 100 players against each other in a struggle for survival. Gather supplies and outwit your opponents to become the last person standing.</p>
        <GameButtons>
        <Button type="default" shape="round"  size={"large"}>
          100 views 
        </Button>
        <Button type="primary" shape="round"  size={"large"}>
          66 likes 
        </Button>
        <Button type="primary" shape="round"  size={"large"}>
          Add to Your Wish List 
        </Button>
        </GameButtons>
      </GameDetailsWrapper>
      <GameCommentsWrapper>
        <h2>Comments</h2>
        <Comment />
        <Comment />
      </GameCommentsWrapper>
      <InputCommentWrapper>
        <Input.TextArea bordered={false} style={{resize: "none"}} placeholder="leave your comment" rows={4}>
        </Input.TextArea>
        <InputCommentRow >
          <Rate defaultValue={3} />
          <Button type="primary" shape="round">
          Submit 
          </Button>
        </InputCommentRow>
      </InputCommentWrapper>
    </div>
  )
}

function Comment(props) {

  return (
    <div>
      <p style={commentContent}>Game was fun until they gave up on fending off the hackers. Sure it's easy to kill some of the hackers, but it's not fun. The player base died out and it was taking like 1-5 minutes to que into a game.</p>
      <span style={{marginRight: '15px'}}>user: panghh</span><span>rate: 5</span>
    </div>
  )
}

const GameDetailsWrapper = styled.div`
  width: 800px;
  height: 250px;
  margin: 0 auto 50px auto;
`
const GameButtons = styled.div`
  display: flex;
  justify-content: space-around;
`
const GameCommentsWrapper = styled.div`
  width: 800px;
  margin: 0 auto 50px auto;
`
const commentContent = {
  margin: "0",
  padding: "0",
  fontSize: "16px"
}

const InputCommentWrapper = styled.div`
  width: 800px;
  height: 200px;
  margin: 0 auto 50px auto;
  padding: 20px;
  border: 1px solid;
  
`
const InputCommentRow = styled.div`
  height: 60px;
  display: flex;
  align-items: center;

  & ul {
    padding-left: 11px;
  }

  & button {
    margin-left: auto;
    margin-right: 20px;
  }
`