login_mutations = """
                    mutation($email: String!,$password: String!){
                      login(email:$email, password:$password)
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
"""

register_mutation = """
                    mutation ($email: String!,$password1: String!,
                                $password2: String!,$name: String!){
                      register(email: $email,password1: $password1,
                                password2: $password2,name: $name)
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
"""

verifyTokenMutation = """
            mutation($token: String!) {
              verifyToken(token: $token) {
                ...on PayloadType{
                  payload{
                    exp
                    origIat
                    email
                  }
                }
              }
            }
"""


sendForgotPassword = """
            mutation ($email: String!){
              sendForgotPassword(email:$email)
              {
                ...on SuccessType{
                  message
                }
                ...on ErrorType{
                  message
                }
              }
             }
 """


VerifyForgotPassword = """
            mutation ($email: String!,$code: String!){
              verifyForgotPassword(email:$email, code:$code)
              {
                ...on VerifyForgotPasswordSuccessType{
                  token
                }
                ...on ErrorType{
                  message
                }
              }
             }
 """


ChangePassword = """
            mutation ($password1: String!,$password2: String!){
              changePassword(password1:$password1, password2:$password2)
              {
                ...on SuccessType{
                  message
                }
                ...on ErrorType{
                  message
                }
              }
             }
 """

setAvatar = """
                    mutation ($file: Upload!){
                      setAvatar(file:$file)
                      {
                        ...on SuccessType{
                          message
                        }
                        ...on ErrorType{
                          message
                        }
                      }
                    }
"""
