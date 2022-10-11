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
  }
  }
`;