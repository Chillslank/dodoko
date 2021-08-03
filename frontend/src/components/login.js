import React from 'react'
import styled from 'styled-components'
import { Form, Input, Button } from 'antd';

export function Login() {

  const onFinish = (values) => {
    console.log('Success:', values);
  };

  const onFinishFailed = (errorInfo) => {
    console.log('Failed:', errorInfo);
  };

  return (
    <LoginWraper>
      <LoginText>
        Log in
      </LoginText>
      <LoginFormWrapper>
        <Form
          name="basic"
          labelCol={{ span: 8 }}
          wrapperCol={{ span: 22 }}
          initialValues={{ remember: true }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          layout="vertical"
          size="large"
          style={{paddingLeft: "10%"}}
        >
          <Form.Item
            label="Username"
            name="username"
            rules={[{ required: true, message: 'Please input your username!' }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Password"
            name="password"
            rules={[{ required: true, message: 'Please input your password!' }]}
          >
            <Input.Password />
          </Form.Item>
          

          <Form.Item wrapperCol={{ offset: 8, span: 16 }}>
            <Button type="primary" htmlType="submit">
              Submit
            </Button>
          </Form.Item>
        </Form>
      </LoginFormWrapper>

    </LoginWraper>
  )
}

const LoginWraper = styled.div`
  width: 500px;
  height: 600px;
  margin: 0 auto;
  border: 1px solid; 
`
const LoginText = styled.div`
  height: 100px;
  font-size: 18px;
  display: flex;
  justify-content: center;
  align-items: center;
`
const LoginFormWrapper = styled.div`
  height: 600px;
  padding: 0 50px;
`