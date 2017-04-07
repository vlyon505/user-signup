UserForm = """
<h1>Join The Party! Sign Up Here</h1>

<form action="/welcome" method="post">
<table>
    <tbody>
        <tr>
            <td>
                <label for="username">Username</label>
            </td>
            <td>
                <input name="username" type="text" value= {{username}}>
            </td>
            <td class="error">
            {{error_username}}
        </tr>
        <tr>
            <td>
                <label for="password">Password</label>
            </td>
            <td>
                <input name="password" type="password" value="">
            </td>
            <td class="error">
            {{error_password}}
        </tr>
        <tr>
            <td>
                <label for="verify">Verify Password</label>
            </td>
            <td>
                <input name="verify" type="password" value="">
            </td>
            <td class="error">
            {{error_verify}}
        </tr>
        <tr>
            <td>
                <label for="email">Email (optional)</label>
            </td>
            <td>
                <input name="email" type="email" value={{email}}>
            </td>
            <td class="error">
            {{error_email}}
        </tr>
    </tbody>
</table>
<input type="submit">
</form>"""
