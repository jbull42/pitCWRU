import { useLoaderData, Outlet } from "react-router-dom";

const Results = () => {
    // const races = useLoaderData();
    return (
        <>
            <h1>Results</h1>

            <Outlet />
        </>
    );
}
export default Results;