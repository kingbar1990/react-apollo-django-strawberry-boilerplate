import React, {useState, useEffect } from "react";
import { connect } from "react-redux";
import { useMutation } from '@apollo/client';
import { verifyToken, getMe } from "../api/queries/index";
import { VERIFY_TOKEN } from "../api/mutations/index";

export const isAuth = WrappedComponent => {
  const Comp = (props) => {

    const [state, setState] = useState({
      user: null
    });

    const [mutateVerifyToken, { data,  loading, error }] = useMutation(VERIFY_TOKEN);

    useEffect(()=>{
      const onWrappLoaded = async () => {
        try {
          mutateVerifyToken({variables: {
            token: localStorage.getItem('token')
          }});
          const me = await getMe(localStorage.getItem('token'))
  
          setState({user: me.data} )
  
          if(!data.verified)  {
            props.history.push("/login")
          }
        } catch (error) {
          console.log("error", error);
        }
      }
      onWrappLoaded()
    },[])

    return (
      <WrappedComponent {...props} user={state.user} />
    )
  }
  const mapStateToProps = state => ({
    data: state.user
  });
  return connect(mapStateToProps, null)(Comp);
};
