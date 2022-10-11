export const updateTokenExpirationDate = tokenExpirationDate => {
    localStorage.removeItem('token-exp');
    localStorage.setItem('token-exp', tokenExpirationDate);
};

export const getTokenInternal = () => {
    const data = localStorage.getItem('token');
    const token = (data && JSON.parse(data).token) || '';

    return token;
};

export const saveTokenData = token => {
    const timestamp = +new Date();
    const data = JSON.stringify({ token, timestamp });

    localStorage.setItem('token', data);
};

export const isExpired = exp => {
    if (!exp) return false;

    return Date.now() > exp;
};

export const getExpirationDate = token => {
    if (!token) return null;

    const jwt = JSON.parse(Buffer.from(token.split('.')[1], 'base64'));

    return (jwt && jwt.exp && jwt.exp * 1000) || null;
};
