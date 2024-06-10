import React from "react";
import ReactDOM from "react-dom/client";
import FeatureOne from "./FeatureOne";
import FeatureTwo from "./FeatureTwo";
import FeatureThree from "./FeatureThree";
import "./index.css";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <>
    <FeatureOne />
    <FeatureTwo />
    <FeatureThree />
  </>
);
