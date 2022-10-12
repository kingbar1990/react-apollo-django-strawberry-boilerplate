import React, {useState, useEffect } from "react";
import { useHistory } from "react-router-dom";
import { connect } from "react-redux";
import { useMutation, useQuery } from '@apollo/client';
import { verifyToken, getMe } from "../api/queries/index";
import { VERIFY_TOKEN, ME } from "../api/mutations/index";

export const isAuth = WrappedComponent => {
  const Comp = (props) => {

    const history = useHistory();

    const [state, setState] = useState({
      user: null
    });

    const [mutateVerifyToken, { data,  loading, error }] = useMutation(VERIFY_TOKEN);
    const {loading: dataLoading, data: userData, } = useQuery(ME);

    useEffect(()=>{
      const onWrappLoaded = async () => {
        try {
          if (localStorage.getItem('token')) {
            mutateVerifyToken({variables: {
              token: localStorage.getItem('token'),
            }});
          } else {
            history.push("/login")
          }

        } catch (error) {
          console.log("error", error);
        }
      }
      onWrappLoaded()
    },[])

    useEffect(()=>{
      if(userData) {
        setState(userData)
      }
      if (error?.message) {
        history.push("/login")
      }
    },[userData, error])

    return (
      <WrappedComponent {...props} user={state.user} />
    )
  }
  const mapStateToProps = state => ({
    data: state.user
  });
  return connect(mapStateToProps, null)(Comp);
};
