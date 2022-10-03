queryMe = """
        query me{
          me{
            ...on MeType{
              user{
                email
              }
            }
            ...on ErrorType{
              message
            }
          }
        }
"""

queryUsers = """
                query users{
              users{
              email
              }
                }
"""

queryFindUser = """
        query findUser($email: String!){
          findUser(email:$email){
            email
          }
        }
"""
