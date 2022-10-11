import React, { useEffect, useState } from "react";
import swal from "sweetalert";
import { useMutation } from '@apollo/client';
import { useHistory } from "react-router-dom";

import { connect } from "react-redux";
import { Container } from "reactstrap";
import { LoginForm } from "../../components/Forms/LoginForm/index";

import { LOGIN } from "../../api/mutations/index";

const Login = props => {
  const history = useHistory();
  const [mutateLogin, { data,  loading, error }] = useMutation(LOGIN);

  const [errorMessage, setError] = useState(null)

  const onLoginMutation = () => {
    if (data.login?.user?.id) {
      console.log(data)
      props.dispatch({ type: "SET_TOKEN", payload: data.login?.token });
      localStorage.setItem("token", data.login?.token);
      history.push("/dashboard");
    } else if (data.login?.message) {
      setError(data.login?.message)
      console.log(error)
      // const errors = {};
      // const errorData = error.response.data;
      // for (const key in errorData) {
      //   if (errorData.hasOwnProperty(key)) {
      //     const element = errorData[key];
      //     errors[key] = element.toString();
      //   }
      // }
    }
  }

  useEffect(() => {
    (data || error) && onLoginMutation()
  },[data, error])

  const handleLogin = async values => {
    console.log("values",values)
    mutateLogin({variables: {
      email: values.email,
      password: values.password,
    }})
    try {
      
      
        // await login(values)
        // .then(response => {
        //   if (response.status === 200) {
        //     props.dispatch({ type: "SET_TOKEN", payload: response.data.key });
        //     localStorage.setItem("token", response.data.key);
        //     props.history.push("/dashboard");
        //   }
        // })
        // .catch(error => {
        //   const errors = {};
        //   const errorData = error.response.data;
        //   for (const key in errorData) {
        //     if (errorData.hasOwnProperty(key)) {
        //       const element = errorData[key];
        //       errors[key] = element.toString();
        //     }
        //   }
        //   swal({
        //     icon: "error",
        //     title: "Ooops something wrong!",
        //     text: errors.non_field_errors
        //   });
        // });
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <Container>
      <LoginForm 
        login={handleLogin}
        errorMessage={errorMessage}
      />
    </Container>
  );
};

const mapStateToProps = state => ({
  data: state.user
});

export default connect(mapStateToProps)(Login);
