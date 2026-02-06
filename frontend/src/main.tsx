import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import RootLayout from './layouts/RootLayout.tsx'
import Home from './pages/Home.tsx'
import About from './pages/About.tsx'
import Telemetry from './pages/Telemetry.tsx'
import Results from './pages/Results.tsx'
import RaceResults from './pages/RaceResults.tsx'
import 'bootstrap/dist/css/bootstrap.min.css';

const router = createBrowserRouter([
  {
    path: "/",
    element: <RootLayout />,
    children: [
      {index: true, element: <Home />},
      {path: "about", element: <About />},
      {path: "telemetry", element: <Telemetry />},
      {
        path: "race",
        element: <Results />, 
        children:[
        {path: ":raceId", element: <RaceResults />}
        ] 
      }
    ]
  }
]);

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
);
