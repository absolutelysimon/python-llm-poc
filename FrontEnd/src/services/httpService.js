import axios from "axios";

class HttpService {
  constructor(baseURL) {
    this.axiosInstance = axios.create({
      baseURL: baseURL || "http://localhost:5000",
      headers: {
        "Content-Type": "application/json",
      },
    });

    this.axiosInstance.interceptors.request.use(
      (config) => {
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    this.axiosInstance.interceptors.response.use(
      (response) => response.data,
      (error) => {
        let errorMessage = "An error occurred. Please try again later.";
        if (error.response) {
          errorMessage = error.response.data.message || errorMessage;
        } else if (error.request) {
          errorMessage = "No response from server.";
        } else {
          errorMessage = error.message;
        }
        return Promise.reject(new Error(errorMessage));
      }
    );
  }

  async get(url, config = {}) {
    try {
      const response = await this.axiosInstance.get(url, config);
      return response;
    } catch (error) {
      throw new Error(error.message);
    }
  }

  async post(url, data, config = {}) {
    try {
      const response = await this.axiosInstance.post(url, data, config);
      return response;
    } catch (error) {
      throw new Error(error.message);
    }
  }

  async put(url, data, config = {}) {
    try {
      const response = await this.axiosInstance.put(url, data, config);
      return response;
    } catch (error) {
      throw new Error(error.message);
    }
  }

  async delete(url, config = {}) {
    try {
      const response = await this.axiosInstance.delete(url, config);
      return response;
    } catch (error) {
      throw new Error(error.message);
    }
  }
}
const httpService = new HttpService();

export default httpService;
