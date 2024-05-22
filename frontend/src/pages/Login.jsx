import Form from "../components/FormLogin"

function Login() {
    return <Form route="/api/token/" method="login" />
}

export default Login