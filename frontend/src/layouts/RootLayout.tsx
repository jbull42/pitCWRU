import { Outlet } from "react-router-dom";
import AppNavbar from "../components/Navbar";
import { Container } from "react-bootstrap";

export default function RootLayout(){
    return (
        <>
            <AppNavbar />
            <Container className="m-0">
                <header>
                    <h1>My App</h1>
                </header>
                
                <main>
                    <Outlet />
                </main>
            </Container>
        </>
    );
}