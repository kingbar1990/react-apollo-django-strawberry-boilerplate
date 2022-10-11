// // import { composeExecutionErrorMessage, showAlert } from 'utils/index';
// import { default as apolloClient } from './index';
// import { useHistory } from "react-router-dom";
// // import * as path from "./../constants/routes";

// export const client = {
//     query: (options) => {
//         const { query, context, variables, fetchPolicy } = options;
//         return apolloClient
//             .query({
//                 query,
//                 context,
//                 variables,
//                 fetchPolicy,
//             })
//             .then((response) => {
//                 const objectKey = Object.keys(response.data)[0];
//                 const data = response.data[objectKey];
//                 if (data) {
//                     return Promise.resolve(data);
//                 }
//             })
//             .catch((err) => {
//                 return Promise.reject(err);
//             });
//     },
//     mutate: (options) => {
//         const { mutation, context, variables, fetchPolicy, refetchQueries } = options;
//         return apolloClient
//             .mutate({
//                 mutation,
//                 context,
//                 variables,
//                 fetchPolicy,
//                 refetchQueries,
//             })
//             .then((response) => {
//                 return Promise.resolve(response);
//             })
//             .catch((error) => {
//                 // const errorMessage = composeExecutionErrorMessage(error);
//                 // showAlert('Error!', errorMessage);

//                 // return Promise.reject({
//                 //     data: errorMessage,
//                 //     from: mutation.definitions[0].name.value,
//                 // });
//             });
//     },
//     clearStore: () => apolloClient.clearStore(),
// };
