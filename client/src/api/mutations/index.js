// import gql from "graphql-tag";
import { gql } from '@apollo/client';

export const LOGIN = gql`
mutation login($email: String!, $password: String!){
    login(email: $email, password: $password)
    {
    ... on LoginSuccessType{
      user{
        id
        email
      }
      token
    }
    ... on ErrorType{
      message
    }
  }
  }
`;

export const REGISTER = gql`
mutation register ($email: String!, $password1: String!,
$password2: String!, $name: String!){
  register(email: $email, password1: $password1,
    password2: $password2, name: $name)
  {
  ... on RegisterSuccessType{
    user{
      id
      email
    }
    token
  }
  ... on ErrorType{
    message
  }
}
}
`;
