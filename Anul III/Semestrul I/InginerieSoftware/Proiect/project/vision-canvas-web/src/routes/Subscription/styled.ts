import styled from 'styled-components';

export const LocalComponents = {
  Container: styled.div`
    .subscription-card {
      width: 300px;
      border: 1px solid #ddd;
      border-radius: 10px;
      padding: 20px;
      text-align: center;
      box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
      background-color: #fff;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }

    .subscription-title {
      font-size: 24px;
      margin-bottom: 10px;
    }

    .subscription-price {
      font-size: 32px;
      color: #333;
      margin-bottom: 20px;
    }

    .subscription-features {
      list-style-type: none;
      padding: 0;
      margin-bottom: 20px;
    }

    .subscription-features li {
      margin-bottom: 10px;
    }

    .subscription-type {
      font-size: 14px;
      color: #666;
      margin-bottom: 20px;
    }

    .subscription-button {
      background-color: #007bff;
      color: #fff;
      border: none;
      padding: 10px 20px;
      border-radius: 5px;
      cursor: pointer;
      text-decoration: none;
    }

    .subscription-button:hover {
      background-color: #0056b3;
    }
  `,
};
