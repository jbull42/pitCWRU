import { Navbar, Nav, Container } from "react-bootstrap";
import { Link } from "react-router";

export default function AppNavbar(){
    return(
        <Navbar>
            <Container className="m-0">
                <Nav>
                    <Navbar.Brand as={Link} to="/"><img src="/pitCWRUlogo.svg" width="50" height="50" /></Navbar.Brand>
                    <Nav.Link as={Link} to="/telemetry">Telemetry</Nav.Link>
                    <Nav.Link as={Link} to="/about">About</Nav.Link>
                </Nav>
            </Container>
        </Navbar>
    );
}