import Header from '../../components/Header';
import { Box } from '@mui/material';
import { useContext } from 'react';
import { UserContext, SidebarContext } from '../../App';
import { Navigate } from 'react-router-dom';

const ViewForm = ( {formID} ) => {
    const { user, pendingForms } = useContext(UserContext);
    const { setSelected } = useContext(SidebarContext);

    setSelected("View Form");
    
    // console.log(pendingForms);
    // console.log(formID)

    return (
        <>
        {!user ? <Navigate to='/login'/> : <></>}
        {!formID ? <Navigate to='/active'/> : <></>}
        </>
    );
};

// ViewForm.defaultProps = { formID: null}

export default ViewForm;