import * as Yup from "yup";
import { MIN_PASSWORD_LENGTH } from "../../../constants/index";

export const LoginSchema = Yup.object().shape({
  email: Yup.string()
    .email("E-mail is not valid!")
    .required("E-mail is required!"),
  password: Yup.string()
    .min(
      MIN_PASSWORD_LENGTH,
      `Password has to be longer than ${MIN_PASSWORD_LENGTH} characters!`
    )
    .required("Password is required!")
});
