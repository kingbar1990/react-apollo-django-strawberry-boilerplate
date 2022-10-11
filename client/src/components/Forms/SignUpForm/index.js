import React from "react";
import { Formik, Form, Field } from "formik";
import { Button } from "reactstrap";
import { ReactstrapInput } from "reactstrap-formik";

import { SignupSchema } from "./validation";

export const SignUpForm = props => (
  <Formik
    initialValues={{
      username: "",
      email: "",
      password1: "",
      password2: ""
    }}
    validationSchema={SignupSchema}
    onSubmit={props.register}
  >
    {() => (
      <div className="card">
        <div className="card-header">Signup</div>
        <div className="card-body">
          <Form>
            <Field
              name="username"
              type="text"
              component={ReactstrapInput}
              label="Name"
            />
            <Field
              name="email"
              type="email"
              component={ReactstrapInput}
              label="Email"
            />
            <Field
              name="password1"
              type="password"
              component={ReactstrapInput}
              label="Password"
            />
            <Field
              name="password2"
              type="password"
              component={ReactstrapInput}
              label="Password confirmation"
            />
            <div className="d-flex align-items-center">
              <Button type="submit">Submit</Button>
              <p style={{color:'red'}} className="mb-0 ml-3">{props.errorMessage}</p>
            </div>
          </Form>
        </div>
      </div>
    )}
  </Formik>
);
