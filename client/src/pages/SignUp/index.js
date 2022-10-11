import React, { useEffect, useState } from "react";
import { useHistory } from "react-router-dom";
import { useMutation } from '@apollo/client';

import * as path from "../../constants/routes";
import {Container} from "reactstrap";

import {SignUpForm} from "../../components/Forms/SignUpForm/index";
import swal from "sweetalert";
import {signUp} from "../../api/queries/index.js";
import { REGISTER } from "../../api/mutations/index";

const SignUp = props => {
    const history = useHistory();
    const [mutateRegister, { data,  loading, error }] = useMutation(REGISTER);

    const [errorMessage, setError] = useState(null);

    const onLoginMutation = () => {
        if (data.register?.user?.id) {
            history.push(path.DASHBOARD);
        } else if (data.register?.message) {
            setError(data.register?.message)
          // const errors = {};
          // const errorData = error.response.data;
          // for (const key in errorData) {
          //   if (errorData.hasOwnProperty(key)) {
          //     const element = errorData[key];
          //     errors[key] = element.toString();
          //   }
          // }
          console.log(error)
        }
      }

    useEffect(() => {
        (data || error) && onLoginMutation()
      },[data, error])

    const handleSignUp = async (values, {setErrors}) => {
        try {
            mutateRegister({variables: {
                email: values.email,
                name: values.username,
                password1: values.password1,
                password2: values.password2,
            }})

            // await signUp(values)
            //     .then(response => {
            //         if (response.status === 201) {
            //             props.history.push(path.DASHBOARD);
            //         } else {
            //             swal({
            //                 icon: "error",
            //                 title: "Ooops something wrong!",
            //                 text: "Please try again"
            //             });
            //         }
            //     })
            //     .catch(error => {
            //         const errors = {};
            //         const errorData = error.response.data;
            //         for (const key in errorData) {
            //             if (errorData.hasOwnProperty(key)) {
            //                 const element = errorData[key];
            //                 errors[key] = element.toString();
            //             }
            //         }
            //         setErrors(errors);
            //     });
        } catch (error) {
            console.error(error);
        }
    };

    return (
        <Container>
            <SignUpForm 
                register={handleSignUp}
                errorMessage={errorMessage}
            />
        </Container>
    );
};

export default SignUp;
