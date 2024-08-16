import { useDispatch } from "react-redux";

const contactFormSchema = Yup.object().shape({
        nameInput: Yup.string().min(2, "Too Short!").max(12, "Too Long!").required("Required"),
        passwordInput: Yup.number().required("Required")
    });
return (
        <Formik initialValues={{ name: "", phone: "" }} onSubmit={handleSubmit} validationSchema={registerFormSchema}>
            <Form className={css.form}>
                <div className={css.inputBox}>
                    <label htmlFor="username" className={css.label}>Username</label>
                    <Field type='text' name='name' id='username'className={css.input}></Field>
                    <ErrorMessage name='name' component='span' className={css.error}/>
                </div>
                <div  className={css.inputBox}>
                    <label htmlFor="password" className={css.label}>Phone number</label>
                    <Field type='number' name='password' id='password' className={css.input}></Field>
                    <ErrorMessage name='password' component='span' className={css.error}/>
                </div>
                
                <button type='submit' className={css.btnAdd}>submit</button>
            </Form>
        </Formik>
)