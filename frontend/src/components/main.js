import React from 'react'
import styled from 'styled-components'
import { Input } from 'antd';
import 'antd/dist/antd.css';

const { Search } = Input;


export function Main() {
  const onSearch = () => {

  }

  return (
    <MainWrapper>
      <MainLogo>

      </MainLogo>
      <MainSearch>
        <Search placeholder="input search text" onSearch={onSearch} allowClear enterButton="Search" size="large" style={{width: "40%"}}/>
      </MainSearch>
      <MainContentWraper>
        <MainContentItem>
        </MainContentItem>
        <MainContentItem>
        </MainContentItem>
      </MainContentWraper>
    </MainWrapper>
  )
}

const MainWrapper = styled.div`
  padding: 0 100px;
  height: 800px;
`
const MainLogo = styled.div`
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
`
const MainSearch = styled.div`
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
`
const MainContentWraper = styled.div`
  display: flex;
  height: 600px;
  justify-content: center;
`
const MainContentItem = styled.div`
  width: 30%;
  margin-right: 40px;
`