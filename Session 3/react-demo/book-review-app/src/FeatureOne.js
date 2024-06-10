import { useState } from "react";

const FeatureOne = () => {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h1>{count}</h1>
      <button onClick={() => setCount(count + 1)}>Add</button>
    </div>
  );
};

export default FeatureOne;
