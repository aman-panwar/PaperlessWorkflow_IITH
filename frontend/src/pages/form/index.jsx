import Header from '../../components/Header';
import { Box, Button, TextField } from '@mui/material';
import { Formik } from 'formik';
import * as yup from "yup";
import useMediaQuery from '@mui/material/useMediaQuery';

const initialValues = {
    firstName: "",
    lastName: "",
    email: ""
};

// const emailRegExp = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
const formSchema = yup.object().shape({
    firstName: yup.string().required("required"),
    lastName: yup.string().required("required"),
    email: yup
            .string()
            // .matches(emailRegExp, "invalid email")
            .email("invalid email")
            .required("required"),
});

const Form = () => {
    const isNonMobile = useMediaQuery("(min-width:600px)");

    const handleFormSubmit = (values) => {
        console.log("Submitted Form!")
        console.log(values)
    }

    return (
        <Box m="20px">
            {/* <Box display="flex" justifyContent="space-between" alignItems="center"> */}
            <Header title="FORM" subtitle="Enter the details and submit the form."/>
            <br></br>
            <Formik
                onSubmit={handleFormSubmit}
                initialValues={initialValues}
                validationSchema={formSchema}
            >
                {({ values, errors, touched, handleBlur, handleChange, handleSubmit }) => (
                    <form onSubmit={handleSubmit}>
                        <Box 
                            display="grid" 
                            gap="30px" 
                            gridTemplateColumns="repeat(4, minmax(0, 1fr))"
                            sx = {{
                                "& > div": { gridColumn: isNonMobile ? undefined : "span 4" },
                            }}
                        >
                            <TextField
                                fullWidth
                                variant="filled"
                                type="text"
                                label="First Name"
                                onBlur={handleBlur}
                                onChange={handleChange}
                                value={values.firstName}
                                name="firstName"
                                error={!!touched.firstName && !!errors.firstName}
                                helperText={touched.firstName && errors.firstName}
                                sx ={{ gridColumn: "span 2" }}
                            />
                            <TextField
                                fullWidth
                                variant="filled"
                                type="text"
                                label="Last Name"
                                onBlur={handleBlur}
                                onChange={handleChange}
                                value={values.lastName}
                                name="lastName"
                                error={!!touched.lastName && !!errors.lastName}
                                helperText={touched.lastName && errors.lastName}
                                sx ={{ gridColumn: "span 2" }}
                            />
                            <TextField
                                fullWidth
                                variant="filled"
                                type="text"
                                label="Email"
                                onBlur={handleBlur}
                                onChange={handleChange}
                                value={values.email}
                                name="email"
                                error={!!touched.email && !!errors.email}
                                helperText={touched.email && errors.email}
                                sx ={{ gridColumn: "span 4" }}
                            />
                        </Box>
                        <Box display="flex" justifyContent="end" mt="20px">
                            <Button type="submit" color="secondary" variant="contained">
                                Submit Form
                            </Button>
                        </Box>
                    </form>
                )}
            </Formik>
        </Box>
    );
    
}

export default Form;