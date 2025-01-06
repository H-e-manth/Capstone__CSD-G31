import { Typography } from '@mui/material';
import { Box } from '@mui/material';
import React from 'react';
import { useSelector } from 'react-redux';
import CardElement from '../../component/CardElement';

const UserJobsHistory = () => {
    const { user } = useSelector(state => state.userProfile);

    console.log(user); // Debugging

    return (
        <>
            <Box>
                <Typography variant="h4" sx={{ color: "#fafafa" }}>
                    Jobs History
                </Typography>
                <Box>
                    {
                        user?.jobsHistory?.length > 0 ? (
                            user.jobsHistory.map((history, i) => (
                                <CardElement
                                    key={i}
                                    id={history?._id || ''}
                                    jobTitle={history?.title || ''}
                                    description={history?.description || ''}
                                    category=""
                                    location={history?.location || ''}
                                />
                            ))
                        ) : (
                            <Typography variant="body1" sx={{ color: "#fafafa" }}>
                                No job history available.
                            </Typography>
                        )
                    }
                </Box>
            </Box>
        </>
    );
};

export default UserJobsHistory;
