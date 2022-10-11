import React from "react";

import { Formik, Form, Field } from "formik";
import { Button } from "reactstrap";
import { ReactstrapInput } from "reactstrap-formik";
import { LoginSchema } from "./validation";

export const LoginForm = ({ login, errorMessage }) => (
  <Formik
    initialValues={{
      email: "",
      password: ""
    }}
    validationSchema={LoginSchema}
    onSubmit={login}
  >
    {() => (
      <div className="card">
        <div className="card-header">Login</div>
        <div className="card-body">
          <Form>
            <Field
              name="email"
              type="email"
              component={ReactstrapInput}
              label="Email"
            />
            <Field
              name="password"
              type="password"
              component={ReactstrapInput}
              label="Password"
            />
            <div className="d-flex align-items-center">
              <Button type="submit">Submit</Button>
              <p style={{color:'red'}} className="mb-0 ml-3">{errorMessage}</p>
            </div>
          </Form>
        </div>
      </div>
    )}
  </Formik>
);
